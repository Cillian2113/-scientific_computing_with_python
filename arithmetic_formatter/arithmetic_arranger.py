def arithmetic_arranger(problems, show = False):
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems
  k=0
  line1=""
  line2=""
  line3=""
  line4=""
  arranged_problems=""
  result=[0]*len(problems)


  while len(problems) > k:
    split = problems[k].split()
    n1=split[0]
    op=split[1]
    n2=split[2]
    length= max(len(n1),len(n2))

    if len(n1) < 5 and len(n2) < 5:
      if n1.isnumeric() and n2.isnumeric():
        if op == '+':
          result[k] = str(int(n1)+int(n2))
          line1+="  "+(length-len(str(n1)))*" "+str(n1)+"    "
          line2+="+ "+(length-len(str(n2)))*" "+str(n2)+"    "
          line3+= (length+2)*"-"+"    "
          line4+=" "+(length-len(result[k])+1)*" "+result[k]+"    "

          k+=1
        elif op == '-':
          result[k] = str(int(n1)-int(n2))
          line1+="  "+(length-len(str(n1)))*" "+str(n1)+"    "
          line2+="- "+(length-len(str(n2)))*" "+str(n2)+"    "
          line3+= (length+2)*"-"+"    "
          line4+=" "+(length-len(result[k])+1)*" "+result[k]+"    "


          k+=1
        else:
          arranged_problems = "Error: Operator must be '+' or '-'."
          return arranged_problems
      else:
        arranged_problems="Error: Numbers must only contain digits."
        return arranged_problems
    else:
      arranged_problems="Error: Numbers cannot be more than four digits."
      return arranged_problems

    #for x in range(len(problems)):
    #  line1="  "+max(n1
  if show == True:
    arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + '\n' + line4.rstrip()
    return arranged_problems
  else:
    arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip()
    return arranged_problems
