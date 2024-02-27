
import user_settings
from CLM5 import case


# Settings
name_case           = 'CLM5_BGC_EUR_0275_spinup_test_JR'
do_case_delete      = True
do_setup_clean      = False
do_build_clean      = False
do_submit           = False


# Main
my_case = case(**getattr(user_settings, name_case))

my_case.create(delete = do_case_delete)
my_case.setup(clean = do_setup_clean)
my_case.config()
my_case.namelists()
my_case.streams()
my_case.build(clean = do_build_clean)

if do_submit: my_case.submit()
