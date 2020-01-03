import sys
import ee_interpreter as eei

if len(sys.argv) > 0 :
    e_file = open(sys.argv[1])

    if e_file.name.endswith(".e") :
        e_file_content_list = e_file.readlines()
        e_code = ""

        for line in e_file_content_list :
            e_code += str(line).replace("\n", "")

        eei.runEE(e_code)
    
    else:
        print(f"File format validn't! Use .e files! Argument 0 : {e_file.name}")
