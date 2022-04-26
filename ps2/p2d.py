(M <= S) and (S <= P) and not(M <= P)
((not M) or S) and (S <= P) and not(M <= P)  # Conditional Identity
((not M) or S) and ((not S) or P) and not(M <= P)  # Conditional Identity
((not M) or S) and ((not S) or P) and not((not M) or P)  # Conditional Identity
(M and ((not M) or S)) and ((not P) and ((not S) and ((not S) or P)))  # Commutative Law
((M and (not M)) or (M and S)) and ((not P and not S) or ((not P) and P))  # Distributive Law
(M and S) and (not P and not S)  # Identity Law
(M and (not P)) and ((not S) and S)  # Associative Law
