#! /bin/env python
#
# Python script to create the product directory recommended by
# Rational Software.
#


import os
import sys
import types


def make_product_dir():
    """
    Make the Rational-recommended product directory in the current
    working directory.
    """
    root = os.path.join('.', 'product_dir')
    try:
        os.makedirs(root)

        businessModeling = os.path.join(root, 'bus_modeling')
        os.makedirs(businessModeling)
        os.makedirs(os.path.join(businessModeling, 'models'))

        deployment = os.path.join(root, 'deployment')
        os.makedirs(deployment)
        os.makedirs(os.path.join(deployment, 'documents'))
        os.makedirs(os.path.join(deployment, 'installation'))
        os.makedirs(os.path.join(deployment, 'manuals'))

        design = os.path.join(root, 'design')
        os.makedirs(os.path.join(design, 'documents'))
        os.makedirs(os.path.join(design, 'models'))
        os.makedirs(os.path.join(design, 'subsystem-1/'))

        os.makedirs(os.path.join(root, 'environment'))
        os.makedirs(os.path.join(root, 'implementation'))
        os.makedirs(os.path.join(root, 'integration'))

        meetings = os.path.join(root, 'meetings')
        os.makedirs(meetings)
        os.makedirs(os.path.join(meetings, 'minutes'))
        os.makedirs(os.path.join(meetings, 'presentations'))

        projectMgt = os.path.join(root, 'proj_mgt')
        os.makedirs(projectMgt)
        os.makedirs(os.path.join(projectMgt, 'assessment'))
        os.makedirs(os.path.join(projectMgt, 'budget_billing'))
        os.makedirs(os.path.join(projectMgt, 'documents'))
        os.makedirs(os.path.join(projectMgt, 'plans'))
        os.makedirs(os.path.join(projectMgt, 'status'))
        
        requirements = os.path.join(root, 'requirements')
        os.makedirs(requirements)
        os.makedirs(os.path.join(requirements, 'database'))
        os.makedirs(os.path.join(requirements, 'documents'))
        os.makedirs(os.path.join(requirements, 'models'))
        os.makedirs(os.path.join(requirements, 'reports'))

        rAndD = os.path.join(root, 'r_and_d')
        os.makedirs(rAndD)

        stds = os.path.join(root, 'stds_guidelines')
        os.makedirs(stds)
        os.makedirs(os.path.join(stds, 'design'))
        os.makedirs(os.path.join(stds, 'documentation'))
        os.makedirs(os.path.join(stds, 'implementation'))
        os.makedirs(os.path.join(stds, 'requirements'))
                             
        test = os.path.join(root, 'test')
        os.makedirs(test)
        
        thirdParty = os.path.join(root, 'third_party_sware')
        os.makedirs(thirdParty)

        tools = os.path.join(root, 'tools')
        os.makedirs(tools)
        os.makedirs(os.path.join(tools, 'config_mgt'))
        os.makedirs(os.path.join(tools, 'dev_env'))
        os.makedirs(os.path.join(tools, 'req_mgt'))
        os.makedirs(os.path.join(tools, 'test'))
        os.makedirs(os.path.join(tools, 'visual_mdling'))
        
    except OSError as ose:
        print("OSError(%s): %s" % (ose.errno, ose.strerror), end=' ')
        if (ose.filename != None):
            print("%s" % (ose.filename))
        else:
            print()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    
if __name__ == '__main__':
    make_product_dir()
