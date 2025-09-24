import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

fig1 = plt.figure()
plt.plot([17, 45, 7, 8, 7], color='orange')

fig2 = plt.figure()
plt.plot([13, 25, 1, 6, 3], color='blue')

Fig3 = plt.figure()
plt.plot([22, 11, 2, 1, 23], color='green')


def save_image(filename):
  

    p = PdfPages(filename)
    
    fig_nums = plt.get_fignums()  
    figs = [plt.figure(n) for n in fig_nums]
    
    for fig in figs: 
      
        fig.savefig(p, format='pdf') 
    
    p.close()  

filename = "multi_plot_image.pdf"  

save_image(filename)
