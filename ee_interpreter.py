def runBF(code):
    memoryLocation = 0
    memory = []
    codePosition = 0
    isJumping = False
    lastBracket = ' '
    for i in range(30000) :
        memory.append(0)
    while codePosition < len(code) or isJumping :
        if memory[memoryLocation] > 255 :
            memory[memoryLocation] -= 256
        if memory[memoryLocation] < 0 :
            memory[memoryLocation] += 256
        if isJumping == False :
            if code[codePosition] == '.' :
                print(chr(memory[memoryLocation]))
            elif code[codePosition] == '+' :
                memory[memoryLocation] += 1
            elif code[codePosition] == '-' :
                memory[memoryLocation] -= 1
            elif code[codePosition] == '>' :
                memoryLocation += 1
                if memoryLocation > len(memory) :
                    print('Memory Location too high. Program stopped')
                    return
            elif code[codePosition] == '<' :
                memoryLocation -= 1
                if memoryLocation < 0 :
                    print('Memory Location too low. Program stopped')
                    return
            elif code[codePosition] == '[' and memory[memoryLocation] == 0 :
                isJumping = True
                lastBracket = code[codePosition]
            elif code[codePosition] == ']' and not memory[memoryLocation] == 0 :
                isJumping = True
                lastBracket = code[codePosition]
            elif code[codePosition] == ',' :
                consoleInput = input()
                if len(consoleInput) > 0 :
                    memory[memoryLocation] = ord(consoleInput[0])
                else :
                    memory[memoryLocation] = 0
        else :
            if codePosition > len(code) - 1 :
                codePosition -= len(code)
            if lastBracket == '[' and code[codePosition] == ']' and memory[memoryLocation] == 0 :
                isJumping = False
            elif lastBracket == ']' and code[codePosition] == '[' and not memory[memoryLocation] == 0:
                isJumping = False
            else :
                pass
        codePosition += 1

def runEE(code):
    memoryLocation = 0
    memory = []
    returnCodePositions = []
    functions = [("re", -1)]
    newFunctionName = ""
    newFunctionPosition = 0
    calledFunctionName = ""
    calledFunctionPositions = []
    accumulator = 0
    codePosition = 0
    isJumping = False
    lastBracket = ' '
    funcDefBracketDiff = 0
    for i in range(30000) :
        memory.append(0)
    while codePosition < len(code) or isJumping :
        if memoryLocation > len(memory)-1:
            return
        if memoryLocation < 0:
            return
        if memory[memoryLocation] > 255 :
            memory[memoryLocation] -= 256
        if memory[memoryLocation] < 0 :
            memory[memoryLocation] += 256
        if isJumping == False :
            if code[codePosition] == '.' :
                if memory[memoryLocation] == 10 :
                    print('')
                else :
                    print(chr(memory[memoryLocation]), end="")
            elif code[codePosition] == '+' :
                memory[memoryLocation] += 1
            elif code[codePosition] == '-' :
                memory[memoryLocation] -= 1
            elif code[codePosition] == '>' :
                memoryLocation += 1
                if memoryLocation > len(memory) :
                    print('Memory Location too high. Program stopped')
                    return
            elif code[codePosition] == '<' :
                memoryLocation -= 1
                if memoryLocation < 0 :
                    print('Memory Location too low. Program stopped')
                    return
            elif code[codePosition] == '[' and memory[memoryLocation] == 0 :
                isJumping = True
                lastBracket = code[codePosition]
            elif code[codePosition] == ']' and not memory[memoryLocation] == 0 :
                isJumping = True
                lastBracket = code[codePosition]
            elif code[codePosition] == ',' :
                consoleInput = input()
                if len(consoleInput) > 0 :
                    memory[memoryLocation] = ord(consoleInput[0])
                else :
                    memory[memoryLocation] = 0
            elif code[codePosition] == '$' :
                accumulator = memory[memoryLocation]
            elif code[codePosition] == '§' :
                memory[memoryLocation] = accumulator
            elif code[codePosition] == '(' :
                isJumping = True
                calledFunctionName = ""
                lastBracket = code[codePosition]
            elif (code[codePosition] == ';' or code[codePosition] == '}') and len(returnCodePositions) > 0 :
                codePosition = returnCodePositions[len(returnCodePositions)-1]
                returnCodePositions.pop(len(returnCodePositions)-1)
                calledFunctionPositions.pop(len(calledFunctionPositions)-1)
            elif code[codePosition] == '"' :
                isJumping = True
                newFunctionName = ""
                lastBracket = code[codePosition]
            elif code[codePosition] == '{' :
                isJumping = True
                newFunctionPosition = codePosition
                functions.append((newFunctionName, newFunctionPosition))
                lastBracket = code[codePosition]
        else :
            if codePosition > len(code) - 1 :
                codePosition -= len(code)
            if lastBracket == '[' and code[codePosition] == ']' and memory[memoryLocation] == 0 and funcDefBracketDiff == 0 :
                isJumping = False
            elif lastBracket == ']' and code[codePosition] == '[' and not memory[memoryLocation] == 0 and funcDefBracketDiff == 0 :
                isJumping = False
            elif lastBracket == '(' :
                if not code[codePosition] == ')' :
                    calledFunctionName += code[codePosition]
                else :
                    functionFound = False
                    for i in range(len(functions)):
                        funcName, funcPos = functions[i]
                        if calledFunctionName == funcName :
                            functionFound = True
                            returnCodePositions.append(codePosition)
                            calledFunctionPositions.append(funcPos)
                            codePosition = funcPos
                    if not functionFound :
                        print("The function '" + calledFunctionName + "' does existn't, dumbass")
                    isJumping = False
            elif lastBracket == '"' :
                if not code[codePosition] == '"' :
                    newFunctionName += code[codePosition]
                else:
                    isJumping = False
            elif lastBracket == '{' :
                if code[codePosition] == '}' : 
                    isJumping = False # 
            if (lastBracket == '[' or lastBracket == ']') and code[codePosition] == '{' and len(returnCodePositions) == 0 :
                funcDefBracketDiff += 1
            if (lastBracket == '[' or lastBracket == ']') and code[codePosition] == '}' and len(returnCodePositions) == 0 :
                funcDefBracketDiff -= 1
            if (lastBracket == '[' or lastBracket == ']') and code[codePosition] == '}' and len(returnCodePositions)> 0 : #
                codePosition = calledFunctionPositions[len(calledFunctionPositions)-1] #
        codePosition += 1 
