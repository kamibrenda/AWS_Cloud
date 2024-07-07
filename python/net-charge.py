# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {'y':10.07, 'c':8.18, 'k':10.53, 'h':6.00, 'r':12.48, 'd':3.65, 'e':4.25}

# Initialize seqCount with 0 for each key
seqCount = {x: float(insulin.count(x)) for x in pKR.keys()}

pH = 0
while pH <= 14:
    netCharge = (+(sum((seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x])) for x in ['k','h','r']))
    -(sum((seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x])) for x in ['y','c','d','e'])))
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1
