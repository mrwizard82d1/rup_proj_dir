#! /bin/env python

#
# Python script to create the product directory recommended by
# Rational Software.
#


import argparse
import os


def make_product_dir(target_dir):
    """
    Create a directory named `target_dir` containing the Rational-recommended product directory in the current
    working directory.
    """
    root = os.path.join('.', target_dir)
    try:
        os.makedirs(root)

        business_modeling = os.path.join(root, 'bus_modeling')
        os.makedirs(business_modeling)
        os.makedirs(os.path.join(business_modeling, 'models'))

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

        project_mgt = os.path.join(root, 'proj_mgt')
        os.makedirs(project_mgt)
        os.makedirs(os.path.join(project_mgt, 'assessment'))
        os.makedirs(os.path.join(project_mgt, 'budget_billing'))
        os.makedirs(os.path.join(project_mgt, 'documents'))
        os.makedirs(os.path.join(project_mgt, 'plans'))
        os.makedirs(os.path.join(project_mgt, 'status'))
        
        requirements = os.path.join(root, 'requirements')
        os.makedirs(requirements)
        os.makedirs(os.path.join(requirements, 'database'))
        os.makedirs(os.path.join(requirements, 'documents'))
        os.makedirs(os.path.join(requirements, 'models'))
        os.makedirs(os.path.join(requirements, 'reports'))

        r_and_d = os.path.join(root, 'r_and_d')
        os.makedirs(r_and_d)

        stds = os.path.join(root, 'stds_guidelines')
        os.makedirs(stds)
        os.makedirs(os.path.join(stds, 'design'))
        os.makedirs(os.path.join(stds, 'documentation'))
        os.makedirs(os.path.join(stds, 'implementation'))
        os.makedirs(os.path.join(stds, 'requirements'))
                             
        test = os.path.join(root, 'test')
        os.makedirs(test)
        
        third_party = os.path.join(root, 'third_party_software')
        os.makedirs(third_party)

        tools = os.path.join(root, 'tools')
        os.makedirs(tools)
        os.makedirs(os.path.join(tools, 'config_mgt'))
        os.makedirs(os.path.join(tools, 'dev_env'))
        os.makedirs(os.path.join(tools, 'req_mgt'))
        os.makedirs(os.path.join(tools, 'test'))
        os.makedirs(os.path.join(tools, 'visual_modeling'))
        
    except OSError as ose:
        print(f"OSError({ose.errno}): {ose.strerror}", end=' ')
        if ose.filename is not None:
            print(f"{ose.filename}")
        else:
            print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target_dir', help='Name of project directory to create')
    args = parser.parse_args()
    make_product_dir(args.target_dir)
