import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages  

with PdfPages("multiple_plots.pdf") as pdf:  
    plt.figure()  
    plt.plot([1, 2, 3], [4, 5, 6], marker='o', linestyle='--', color='r')  
    plt.title("Plot 1")  
    pdf.savefig()    
    plt.close()    
    
    plt.figure()  
    plt.bar(["A", "B", "C"], [10, 20, 30], color="g")  
    plt.title("Plot 2")  
    pdf.savefig()   
    plt.close()  
