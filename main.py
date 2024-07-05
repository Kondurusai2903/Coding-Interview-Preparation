# --------------------------square pattern-----

# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()
# for i in range(n):
#     print("*"*n)

# -------------hallow square pattern-----------
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == 0 or i == 0 or i == n-1 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(n):
#     if i == 0 or i == n-1:
#         print("* "*n)
#     else:
#         print("* "+"  "*(n-2)+"*")
# --------------------left triangle pattern---------
n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# for i in range(1, n+1):
#     print("* "*i+" "*(n-i))

# ---------------------right triangle pattern--------
# n = 5
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

# for i in range(1, n+1):
#     print("  "*(n-i)+"* "*i)

# --------------left downward triangle pattern-------------------------
# n = 5
# for i in range(1, n+1):
#     for j in range(n-i+1):
#         print("*", end=" ")
#     for k in range(i):
#         print(" ", end=" ")
#     print()

# ----------- right downward triangle pattern ---------------------------
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(n-i):
#         print("*", end=" ")
#     print()


# -------------------hallow triangle star pattern----------------------
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if i == j or j == 0 or i == n-1:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()


# -----------------------pyramid pattern -------------------------
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("  ", end="")
#     for k in range(2*i+1):
#         print("* ", end="")
#     print()

# -------------------------Hallow pyramid pattern-------------------
# n = 5
# for i in range(n):
#     for k in range(n-i):
#         print("  ", end=" ")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i or i == n-1:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

# -----------------------Reverse pyramid pattern ------------------------------------
# n = 5
# for i in range(n):
#     for j in range(i):
#         print("  ", end=" ")
#     for k in range(2*(n-i)-1):
#         print("* ", end=" ")
#     print()

# ---------------------------diamond start pattern ----------------------------------------
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("  ", end=" ")
#     for k in range(2*i+1):
#         print("* ", end=" ")
#     print()
# for i in range(1, n+1):
#     for j in range(i+1):
#         print("  ", end=" ")
#     for k in range(2*(n-i-1)+1):
#         print("* ", end=" ")
#     print()
# -------------------------the above and below code are same but difference in the second for loop formula ----------
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("  ", end=" ")
#     for k in range(2*i+1):
#         print("* ", end=" ")
#     print()
# for x in range(1, n+1):
#     for y in range(x+1):
#         print("  ", end=" ")
#     for z in range(2*(n-x)-1):
#         print("* ", end=" ")
#     print()


# ----------------------------------hallow diamond pattern --------------------------------------------
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("  ", end=" ")
#     for k in range(2*i+1):
#         if k == 0 or k == 2*i:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()
# for x in range(1, n+1):
#     for y in range(x+1):
#         print("  ", end=" ")
#     for z in range(2*(n-x)-1):
#         if z == 0 or z == 2*(n-x)-2:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()


# ---------------------hourglass pyramid pattern-----------------------------------
# n = 5
# for i in range(n):
#     for j in range(i):
#         print("  ", end=" ")
#     for k in range(2*(n-i)-1):
#         print("* ", end=" ")
#     print()
# for x in range(1, n):
#     for y in range(n-x-1):
#         print("  ", end=" ")
#     for z in range(2*x+1):
#         print("* ", end=" ")
#     print()


# ---------------------- right pascal's start pattern --------------------------------

# n = 5
# for i in range(1, n+1):
#     for j in range(i):
#         print("* ", end=" ")
#     print()
# for k in range(1, n+1):
#     for l in range(n-k):
#         print("* ", end=" ")
#     print()
# -------------------------------- or--------------------------
# for i in range(1, n+1):
#     print("* "*i)
# for i in range(1, n+1):
#     print("* "*(n-i))

# ----------------------left pascal's start pattern --------------------
# n = 5
# for i in range(1, n+1):
#     for j in range(n-i):
#         print("  ", end=" ")
#     for k in range(i):
#         print("* ", end=" ")
#     print()
# for x in range(n):
#     for y in range(x+1):
#         print("  ", end=" ")
#     for z in range(n-x-1):
#         print("* ", end=" ")
#     print()
# ----------------------------NUmeric diamond pattern-----------------------------------------------
n = 9
for i in range(n):
    for j in range(n-i):
        print("  ", end=" ")
    k = 0
    while (k < i+1):
        print(str(k+1)+" ", end=" ")
        k += 1
    while (k-1 > 0):
        print(str(k-1)+" ", end=" ")
        k -= 1
    print()
for i in range(1, n+1):
    for j in range(i+1):
        print("  ", end=" ")
    k = 0
    while k < 2*(n-i)//2:
        print(str(k+1)+" ", end=" ")
        k += 1
    while k-1 > 0:
        print(str(k-1)+" ", end=" ")
        k -= 1
    print()
