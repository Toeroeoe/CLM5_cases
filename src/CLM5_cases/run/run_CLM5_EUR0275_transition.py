
from CLM5_cases.cases import cases_CLM5_EUR0275_transition
from CLM5_cases.CLM5 import case


# Settings
name_case           = 'CLM5_BGC_EUR_0275_transition'
do_case_delete      = False
do_setup_clean      = False
do_build_clean      = False
do_submit           = True


# Main
my_case = case(**getattr(cases_CLM5_EUR0275_transition, 
                         name_case))

my_case.create(delete = do_case_delete)
my_case.setup(clean = do_setup_clean)
my_case.config()
my_case.namelists()
my_case.streams()
my_case.build(clean = do_build_clean)

if do_submit: my_case.submit()
