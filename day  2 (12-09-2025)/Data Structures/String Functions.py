# Function to trim spaces from the given string
def trim(s: str) -> str:
    return s.strip()

# Function to check if x exists in s and return its index
def exists(s: str, x: str) -> int:
    return s.find(x)

# Function to convert the string into title case
def titleIt(s: str) -> str:
    return s.title()

# Function to swap cases in the string
def casesSwap(s: str) -> str:
    return s.swapcase()


# Example usage:
if __name__ == "__main__":
    s = str(input())   
    x = str(input())

    print(trim(s))       
    print(exists(s, x))  
    print(titleIt(s))    
    print(casesSwap(s))  

