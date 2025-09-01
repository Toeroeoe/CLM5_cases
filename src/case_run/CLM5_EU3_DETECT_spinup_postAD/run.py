import CLM5_EU3_DETECT_spinup_postAD.config as config
from CLM5 import case


# Settings
name_case           = 'test'
do_case_delete      = False
do_setup_clean      = False
do_build_clean      = False
do_submit           = False
do_build            = False


# Main
my_case = case(**getattr(config, 
                         name_case))

my_case.create(delete = do_case_delete)
my_case.setup(clean = do_setup_clean)
my_case.config()
my_case.namelists()
my_case.streams()
if do_build: my_case.build(clean = do_build_clean)

if do_submit: my_case.submit()
