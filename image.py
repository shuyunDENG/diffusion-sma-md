import matplotlib.pyplot as plt

epochs = [
  10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
  110, 120, 130, 140, 150, 160, 170, 180, 190, 200
]
losses = [
  0.396532, 0.393198, 0.392829, 0.393247, 0.388772,
  0.389654, 0.393687, 0.390035, 0.388900, 0.391854,
  0.387915, 0.387468, 0.388547, 0.389427, 0.385475,
  0.385643, 0.387691, 0.385694, 0.386746, 0.387061
]

plt.figure(figsize=(6, 4))
plt.plot(epochs, losses, marker='o')
plt.xlabel('Epoch')
plt.ylabel('MSE Loss')
plt.title('DDPM Training Loss Curve')
plt.grid(True)
plt.tight_layout()
plt.show()