#asher Wangia, Library Notes
import matplotlib.pyplot as plt
import numpy as np
from faker import Faker
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

fake = Faker(['it_IT'])
for _ in range(10):
    print(fake.name())