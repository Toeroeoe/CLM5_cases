
from CLM5_cases.cases import CLM5EU3_split
from CLM5_cases.CLM5 import case


# Settings
name_case           = 'CLM5EU3_BGC_007_east'
do_case_delete      = False
do_setup_clean      = False
do_build_clean      = False
do_submit           = True


# Main
my_case = case(**getattr(CLM5EU3_split, 
                         name_case))

my_case.create(delete = do_case_delete)
my_case.setup(clean = do_setup_clean)
my_case.config()
my_case.namelists()
my_case.streams()
my_case.build(clean = do_build_clean)

if do_submit: my_case.submit()
