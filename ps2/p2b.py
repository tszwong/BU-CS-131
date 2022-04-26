((P <= Q) or (P <= R)) <= (P <= (Q or R))
(((not P) or Q) or ((not P) or R)) <= (P <= (Q or R))  # Conditional Identity
((not P) or (not P) or (Q or R)) <= (P <= (Q or R))  # Associative Law
((not P) or (Q or R)) <= (P <= (Q or R))  # Idempotent Law
(not ((not P) or (Q or R))) or (P <= (Q or R))  # Conditional Identity
(not ((not P) or (Q or R))) or ((not P) or (Q or R))  # Conditional Identity
((not P) or (Q or R)) or (not (not P) or (Q or R))  # Commutative Law

