import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
# Figure dpi
dpi = 72

def plot_cobweb(f, A, x0, nmax=40):
    """Make a cobweb plot.

    Plot y = f(x; r) and y = x for 0 <= x <= 1, and illustrate the behaviour of
    iterating x = f(x) starting at x = x0. A is a parameter to the function.

    """
    x = np.linspace(0, 1, 500)
    fig = plt.figure(figsize=(600/dpi, 450/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    # Plot y = f(x) and y = x
    ax.plot(x, f(x, A), c='#444444', lw=2)
    ax.plot(x, x, c='#444444', lw=2)

    # Iterate x = f(x) for nmax steps, starting at (x0, 0).
    px, py = np.empty((2,nmax+1,2))
    px[0], py[0] = x0, 0



    for n in range(1, nmax, 2):
        px[n] = px[n-1]
        py[n] = f(px[n-1], A)
        px[n+1] = py[n]
        py[n+1] = py[n]

    # for j in range(len(px)):
    #     print("px "+str(px[j][1])+"  py "+str(py[j][1]))
   
    # Plot the path traced out by the iteration.
    ax.plot(px, py, c='b', alpha=0.7)

    # Annotate and tidy the plot.
    ax.minorticks_on()
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('$x$')
    ax.set_ylabel(f.latex_label)
    ax.set_title('$x_0 = {:.1}, A = {:.2}$'.format(x0, A))

    # plt.savefig('cobweb_{:.1}_{:.2}.png'.format(x0, A), dpi=dpi)
    for j in range(len(px)):
        # if j>200:
        print("px "+"%.5f"%px[j][1]+"  py "+"%.5f"%py[j][1])

    print(len(px)) 
    plt.show()


class AnnotatedFunction:
    """A small class representing a mathematical function.

    This class is callable so it acts like a Python function, but it also
    defines a string giving its latex representation.

    """

    def __init__(self, func, latex_label):
        self.func = func
        self.latex_label = latex_label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

# The logistic map, f(x) = Ax(1-x).
func = AnnotatedFunction(lambda x,A: A*x*(1-x), r'$Ax(1-x)$')

###          (A , initial num, num iteration)
# plot_cobweb(func, 0.5, 0.5)
plot_cobweb(func, 3.5, 0.5, 100)# quad
# plot_cobweb(func, 3.58,0.5, 1000)#chaos
# plot_cobweb(func, 3.8, 0.2, 200)