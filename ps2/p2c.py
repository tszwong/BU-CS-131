not((P <= Q) or (Q <= R))
(not(P <= Q)) and (not(Q <= R))  # De Morgan's Law
(not((not P) or Q)) and (not((not Q) or R))  # Conditional Identity
(not(not P) and (not Q)) and (not(not Q) and (not R))  # De Morgan's Law
(P and (not Q)) and (Q and (not R))  # Double Negation Law
(P and (not Q) and Q) and (not R)  # Associative Law
(P and Q and (not Q)) and (not R)  # Commutative Law
