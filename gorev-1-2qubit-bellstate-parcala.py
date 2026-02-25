import numpy as np

# State vector oluşturulması
# bell state
# |Φ+⟩ = 1/√2(|00⟩ + |11⟩)

# baz sırası
# |00>, |01>, |10>, |11>

# Yani vektör:
# (1/√2) * [1, 0, 0, 1]

psi = (1 / np.sqrt(2)) * np.array([1,0,0,1])

print("State Vektör: ", psi)

# Dış Çarpım (Outher Product) ile Density Matrix oluşturulması
# Dış çarpım tanımı: p = |state vektorü>< state vektorü|
rho = np.outer(psi, psi.conj())

print("Density Matrix", rho)

# Partial Trace (İkinci Qubit’i Silmek)
# Burada biraz dikkat.

# 4x4 matrisi 2x2x2x2 şeklinde yeniden şekillendiriyoruz.

# Mantık:

# Sistem boyutu: 2 ⊗ 2

rho_reshaped = rho.reshape(2,2,2,2)
rho_A = np.trace(rho_reshaped, axis1=1, axis2=3)

print("Reduced (Traced) Density Matrix:", rho_A)

# Eigenvalue hesaplamak:
eigenvalues = np.linalg.eigvals(rho_A)

print("Reduced Density Matrix'in eigenvalue'leri:", eigenvalues)

# Von Neumann Entropy
# formül: S=−∑λlog2​λ
# Burada λ=Eigenvalue ve ∑ toplam anlamına geliyor.
entropy = -np.sum(eigenvalues * np.log2(eigenvalues))

print("Von Neumann Entropy:", entropy)

# 2. soru: Reduced density matrix [0.5, 0, 0, 0.5] ise eigenvalue'ları nedir? ve Entropi kaç çıkar?
rho_A2 = [[0.5, 0], [0, 0.5]]

eigenvalues2 = np.linalg.eigvals(rho_A2)

print("Reduced Density Matrix 2'nin eigenvalue'leri: ", eigenvalues2)

entropy2 = -np.sum(eigenvalues2 * np.log2(eigenvalues2))

print("Von Neumann Entropy 2: ", entropy2)

# 3. soru: Eğer reduced density matrix’in eigenvalue’ları [0.8, 0.2] olsaydı, Entropi yaklaşık kaç olurdu?
# Bu sistem Bell state kadar entangled olur muydu?
rho_A3 = [[0.8, 0], [0, 0.2]]

eigenvalues3 = np.linalg.eigvals(rho_A3)

print("Reduced Density Matrix 3'ün eigenvalue'leri: ", eigenvalues3)

entropy3 = -np.sum(eigenvalues3 * np.log2(eigenvalues3))

print("Von Neumann Entropy 3: ", entropy3)

# 4. soru
rho_A4 = [[1, 0], [0, 0]]

eigenvalues4 = np.linalg.eigvals(rho_A4)

print("Reduced Density Matrix 4'ün eigenvalue'leri: ", eigenvalues4)

entropy4 = -np.sum(eigenvalues4[eigenvalues4 > 0] * np.log2(eigenvalues4[eigenvalues4 > 0]))

print("Von Neumann Entropy 4: ", entropy4)

# 5. soru: Şu global state’i al: ∣Ψ⟩=1/√2​(∣00⟩+∣01⟩)
# baz sırası:
# |00>, |01>, |10>, |11>

# Yani vektör:
# (1/√2) * [1, 1, 0, 0]

# 1️⃣ Bu entangled mı?
# 2️⃣ Reduced density matrix ne çıkar?
# 3️⃣ Entropi kaç olur?

psi5 = (1 / np.sqrt(2)) * np.array([1, 1, 0, 0])
rho5 = np.outer(psi5, psi5.conj())

print("Density Matrix 5: ", rho5)

rho5_reshaped = rho5.reshape(2, 2, 2, 2)
rho_A5 = np.trace(rho5_reshaped, axis1=1, axis2=3)

print("Reduced Density Matrix 5: ", rho_A5)

eigenvalues5 = np.linalg.eigvals(rho_A5)

eigenvalues5 = np.real(eigenvalues5)
eigenvalues5 = eigenvalues5[eigenvalues5 > 1e-12]

print("Reduced Density Matrix 5'in eigenvalue'ları: ", eigenvalues5)

entropy5 = -np.sum(eigenvalues5 * np.log2(eigenvalues5))
entropy5 = np.real_if_close(entropy5)
entropy5 = np.round(entropy5, 10)

print("Von Neumann Entropy 5: ", entropy5)