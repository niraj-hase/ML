import numpy as np
def gradient_descent(gradient, start, step, iter, tol=0.01):
	steps = [start]
	x = start
	for _ in range(iter):
		diff = -step*gradient(x)
		if np.abs(diff) <= tol:
			break
		x += diff
		steps.append(x)
	return (step, x, step)
def cost_function(x):
	return x**2+6*x+9
def gradient_func(x):
	return 2*x+6
history, result, learning_rate = gradient_descent(gradient_func, 2, 0.1, 100)

print("steps:",history)
print("minimum:",result)
print("learning rate:",learning_rate)
print("iterations:", len(history))