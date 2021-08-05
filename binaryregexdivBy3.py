import re;
try:
    given_input = input();
except EOFError :
    given_input="";
multiplof3regex = re.compile(r'(0|1(01*0)*1)*');
result = multiplof3regex.search(given_input)
if(result.group() == ""):
    print ("multipleof3Regex (\'{}\') False".format(given_input))
else:
    print ("multipleof3Regex (\'{}\') True".format(given_input))