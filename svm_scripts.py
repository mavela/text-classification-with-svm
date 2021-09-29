import sys
import gzip
from analyze import print_text,read_text


def read_text_ext(inp):
    register = None
    text = []
    for line in inp:
            line=line.strip()
            if line.startswith("# predicted register"):
                if register != None:
                    yield(register, text)
                    text = []
                    register=line.split(":")[1].strip()
                elif register == None:
                    register=line.split(":")[1].strip()
            elif not line.startswith("#"):
                if len(line)== 0:
                    continue
                else:
                    text.append(line.split("\t"))
            else:
                continue
    yield(register, text)
    

def save_text_format(file,col):
    max = 10000
    text_count = 0
    to_return = []
    out_f = open(file+"_out"+".txt","w")
    out_f.write(print_text(file,col,max))
    return
#    print("printed file", out_f)
            
#print("file saved", save_text_format(sys.argv[1],"FORM"))
