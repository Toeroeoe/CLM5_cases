import user_data_arpita_test
from model_cases import CLM5_case


# Settings
name_case           = 'east'
do_case_delete      = False
do_setup_clean      = False
do_build_clean      = False
do_submit           = True


# Main
my_case = CLM5_case(**getattr(user_data_arpita_test, name_case))

my_case.create(delete = do_case_delete)
my_case.setup(clean = do_setup_clean)
my_case.config()
my_case.namelists()
my_case.streams()
my_case.build(clean = do_build_clean)

if do_submit: my_case.submit()
