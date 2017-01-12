# http://arcgisstore1041.s3.amazonaws.com/5686/docs/index.html
# Import modules
import sys
import os.path
import json
import time
from boto import cloudformation

# Functions

def check_status( lo_cform_conn, lc_stack_name ):
    lo_stacks = lo_cform_conn.describe_stacks(lc_stack_name)
    lo_stack = lo_stacks[0]
    lc_cur_status = lo_stack.stack_status
    print "Current status of stack " + lo_stack.stack_name + ": " + lc_cur_status
    for ln_loop in range(1, 9999):
        if "IN_PROGRESS" in lc_cur_status:
            print "\rWaiting for status update(" + str(ln_loop) + ")...",
            time.sleep(1) # pause 1 second

            try:
                lo_stacks = lo_cform_conn.describe_stacks(lc_stack_name)
            except:
                print " "
                print "Stack " + lc_stack_name + " no longer exists"
                lc_cur_status = "STACK_DELETED"
                break

            lo_stack = lo_stacks[0]

            if lo_stack.stack_status != lc_cur_status:
                lc_cur_status = lo_stack.stack_status
                print " "
                print "Updated status of stack " + lo_stack.stack_name + ": " + lc_cur_status
        else:
            break

    return lc_cur_status

# End Functions

# Main program
def main(pc_access_key, pc_secret_key, pc_param_file):

    # Confirm parameters file exists
    if os.path.isfile(pc_param_file):
        lo_json_data=open(pc_param_file).read()
    else:
        print "Parameters file: " + pc_param_file + " is invalid!"
        print " "
        sys.exit(3)

    print "Parameters file: " + pc_param_file
    la_parameters_data = json.loads(lo_json_data)
    lc_region = la_parameters_data["RegionId"]

    # Connect to AWS region specified in parameters file
    print "Connecting to region: " + lc_region
    lo_cform_conn = cloudformation.connect_to_region(lc_region, aws_access_key_id=pc_access_key, aws_secret_access_key=pc_secret_key)

    # Store parameters from file into local variables
    lc_stack_name = la_parameters_data["StackName"]

    # Check if this stack name already exists
    lo_stack_list = lo_cform_conn.describe_stacks()
    ll_stack_exists = False
    for lo_stack in lo_stack_list:
        if lc_stack_name == lo_stack.stack_name:
            print "Stack " + lc_stack_name + " already exists."
            ll_stack_exists = True

    # If the stack already exists then delete it first
    if ll_stack_exists:
        print "Calling Delete Stack API for " + lc_stack_name
        lo_cform_conn.delete_stack(lc_stack_name)

        # Check the status of the stack deletion
        check_status( lo_cform_conn, lc_stack_name )

    print " "
    print "Loading parameters from parameters file:"
    la_create_stack_parameters = []
    for lc_key in la_parameters_data.keys():
        if lc_key == "TemplateUrl":
            lc_template_url = la_parameters_data["TemplateUrl"]
        elif lc_key == "StackName" or lc_key == "RegionId":
            # Do not send as parameters
            print lc_key + " - "+ la_parameters_data[lc_key] + " (not sent as parameter)"
        else:
            print lc_key + " - "+ la_parameters_data[lc_key]
            la_create_stack_parameters.append((lc_key, la_parameters_data[lc_key]))

    # Call CloudFormation API to create the stack
    print " "
    print "Calling CREATE_STACK method to create: " + lc_stack_name

    lc_cur_status = ""

    lc_result = lo_cform_conn.create_stack(stack_name=lc_stack_name, template_body=None, disable_rollback=True, template_url=lc_template_url, parameters=la_create_stack_parameters, capabilities=["CAPABILITY_IAM"])
    print "Output from API call: " + lc_result
    print " "

    # Check the status of the stack creation
    lc_cur_status = check_status( lo_cform_conn, lc_stack_name )

    if lc_cur_status == "CREATE_COMPLETE":
        print "Stack " + lc_stack_name + " created successfully."
    else:
        print "Failed to create stack " + lc_stack_name
        sys.exit(1)

# Call Main program
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "%s:  Error: %s\n" % (sys.argv[0], "Not enough command options given")
        print "Argument 1 (required): AWS Access Key (e.g. ABCDE1FGHIJKL2MNOPQR)"
        print "Argument 2 (required): AWS Secret Access Key (e.g. aBCdE1fGHijKlMn+OPq2RsTUV3wxy45Zab6c+7D8)"
        print "Argument 3 (required): Stack Parameters JSON file (e.g. c:\cloud_formation\cf_stack_parameters.json)"
        print " "
        sys.exit(3)
    else:
        pc_access_key = sys.argv[1]
        pc_secret_key = sys.argv[2]
        pc_param_file = sys.argv[3]

    main(pc_access_key, pc_secret_key, pc_param_file)
