from random import *

prerequisites0102: str = \
"""Pre-requisites [01||02]:
> 1. :: Arithmetic Sequence
        In here, you have to provide any number that'll make a
        sequence of arithmetic numbers, thus each numbers you
        provided must be equally distributed by each differences
        you'll provided it later on.
        
        Usage:
        Each number of sequence has to be separated by spaces,
        and any type of number is allowed except for complex
        numbers and string literals (look for the example down
        below).
        
        Example:
        2 7 4
        ^ ^ ^
        See those three up arrows? That means those are the sequence
        of numbers that will start by only three numbers, then based
        on how many next numbers of sequence will be generated depends
        with the [gen] value you provided.
        
> 2. :: Differences
        Now here in differences section, you have to put the EXACT
        differences of each those example numbers been provided, and
        how it relates to other numbers part of the sequence, and so
        on.
        
        Usage:
        Each diffs on the input MUST HAVE ONLY one arithmetic operation,
        it can be either "+ - * / ** //" (addition, substraction,
        multiplication, division, exponentiation, floor division), then
        followed by numbers that indicates how many the difference in
        between, and if more than one then separate those with spaces
        as you did in the first one at "Arithmetic Sequence" (look for
        the example down below).
        
        Example:
        +5 -3
        ^^ ^^ 
        Based on the example at number 1, "Arithmetic Sequence", here
        is the following differences. "2 7 4" and "+5 -3" is a correct
        differences, because "2 + 5 = 7", and "7 - 3 = 4", thus making
        this as an appropiate providing of both the sequence and the
        differences. 
"""

prerequisites03: str = \
"""Pre-requisites [03]
> 3. :: Generating Count
        Last but not least, here you have to provide on how many
        generation of numbers of sequence, and ONLY integer input
        allowed (look for the example down below).
        
        Usage:
        Provide a single integer value (>={length_of_the_arithmetic
        sequence}).
        
        Example:
        10
        ^^
        That means, 10 numbers in total (including your provided too)
        will be in total of 10 numbers in a sequence. Note that if you
        provided 3 numbers, then it has to be more than 3 generating
        count. If less or negative number input, then it will be an
        invalid generating count input.
"""

def ArithmeticSequence(n: list[int | float], d: list[str], gen: int = 10, qgen: bool = True) -> str:
    assert isinstance(gen, (int))
    assert len(n) - 1 == len(d), "[len(n) - 1] must be equal to [len(d)]"
    
    diff_count: int = 0
    fdn: int = len(n)
    
    for x in range(gen - 1):
        tmp_nd = eval(f"{n[x]}{d[diff_count].replace(' ', '')}")
        diff_count += 1; diff_count = 0 if diff_count == len(d) else diff_count
        try:
            assert tmp_nd == n[x + 1], "the following sequence is NOT a arithmetic sequence!"
            if tmp_nd == n[x + 1]: pass
        except IndexError:
            if str(tmp_nd)[-2:] == '.0': tmp_nd = str(tmp_nd).replace('.0', ''); tmp_nd = int(tmp_nd)
            n.append(tmp_nd)
    
    for i in range(len(n)):
        if str(n[i])[-2:] == '.0': n[i] = int(n[i])
        n[i] = float(f"{n[i]:.5f}") if '.' in str(n[i]) else n[i]
    
    result = QGen(n, fdn) if qgen else 'no apparently any [qgen] solutions were made'
    return f"{n}\n{result}"

def QGen(n: list[int | float], fdn: int) -> list:
    count_true: int = -1
    solved: list[tuple[str, str]] = []
    
    for _ in range(1, len(n)):
        solved.append((f"value={n[count_true]}", f"index={count_true + len(n)}")); n[count_true] = '...'; count_true -= 1
        if abs(count_true) - 1 == fdn: break
    return solved

if __name__ == "__main__":
    while True:
        try:
            n: list[int | float] = list(map(float, input("[01] :: Provide an arithmetic sequence: ").split()))
            d: list[str] = list(map(str, input("[02] :: Provide each difference in between: ").split()))
            gen: int = int(input("[03] :: Provide generating count: "))
            qgen: int = int(input("[04] :: Provide queue generation || <0: False><1: True> ||: "))
            
            if qgen == 1: print(); print(ArithmeticSequence(n, d, gen, qgen=True)); n.clear(); d.clear(); gen = 0; print()
            else: print(); print(ArithmeticSequence(n, d, gen, qgen=False)); n.clear(); d.clear(); gen = 0; print()
        
        except AssertionError: print(prerequisites0102)
        except ValueError: print(); print(prerequisites03)
        except IndexError: print(prerequisites0102)