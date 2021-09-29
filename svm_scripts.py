import sys
import gzip
from analyze import print_text,read_text

def open_fi(file):
    if file.endswith("gz"):
        fl = gzip.open(file, "rt")
    else:
        fl = open(file, "r")
    return(fl)

def print_text_list(llist, col, max):
    cols = ["ID","FORM","LEMMA","UPOS","XPOS","FEAT","HEAD","DEPREL","DEPS","MISC"] #the columns of the conllu format
    to_return = []
    text_count = 0
    for reg, text in llist:
        text_count +=1
        if text_count > max:
            break
        else:
            words = (word_line[cols.index(col)] for word_line in text)
            to_return.append(" ".join(words))
#    return("\n\n".join(to_return))
    return to_return



def split(a,b):
    a_o = open_f(a)
    a_list = []
    b_list = []
    b_o = open_f(b)
    for line in a_o:
        line=line.strip()
        if line.startswith("#"):
            continue
        else:
            line="0" + "\t" + line
            a_list.append(line)
    print("1", print_text_list(a_list,"FORM", 2))
    for line in b_o:
        line=line.strip()
        if line.startswith("#"):
            continue
        else:
            line="1" + "\t" + line
            b_list.append(line)
    print(len(a_list), len(b_list))
    print(a_list[0],b_list[0])


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
    

def save_text_format(file,col, max):
    text_count = 0
    to_return = []
    out_f = open(file+"_out"+".txt","w")
    out_f.write(print_text(file,col,max))
    return
#    print("printed file", out_f)
            
print("file saved", save_text_format(sys.argv[1],"FORM", 10000))
#print(split(sys.argv[1],sys.argv[2]))
