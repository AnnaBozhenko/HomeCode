n = int(input("Enter:"))
fi1 = 0
i = 0
fi2 = 1
fi = 0
if n == fi1:
    i = 1
if n == fi2:
    i =2
while fi < n:
    fi = fi1 + fi2
    fi1 = fi2
    fi2 = fi
    i += 1
print(i)