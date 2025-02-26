
from cases import CLM5_EUR0275_production
from CLM5 import case


# Settings
name_case           = 'CLM5_BGC_EUR_0275_0001'
do_case_delete      = False
do_setup_clean      = False
do_build_clean      = False
do_submit           = True


# Main
my_case = case(**getattr(CLM5_EUR0275_production, 
                         name_case))

my_case.create(delete = do_case_delete)
my_case.setup(clean = do_setup_clean)
my_case.config()
my_case.namelists()
my_case.streams()
my_case.build(clean = do_build_clean)

if do_submit: my_case.submit()
