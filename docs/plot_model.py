import numpy as np
import matplotlib.pyplot as plt

### Import this file for good-looking plots (optional).
plt.style.use('publish.mplstyle')


def plot_model(DIR, profile, history, axp, axh, axh2, axh3, color, label):
    global PATH
    p = np.genfromtxt(PATH + '/' + DIR + '/' + profile, skip_header =5, names=True)
    axp.plot(p["radius"], p["brunt_N2"]/(4*np.pi**2)*1e6, color = color, label = label)
    id_max = np.argmax(p["brunt_N2"])
    axp.plot(p["radius"][id_max], p["brunt_N2"][id_max]/(4*np.pi**2)*1e6, 'o', color = color)

    with open(PATH + '/' + DIR + '/' + profile, 'r') as file:
        header_lines = []
        for line in file:
            line = line.strip()
            if line:
                header_lines.append(line)
            else:
                break

    header_array = np.array(header_lines)

    split_header = np.char.split(header_array)
    num_zones    = split_header[2][0]
    model_number = split_header[2][1]
    print(DIR, 'number of cells: ', num_zones, 'model number at Xc = 0.1: ', model_number)

    h = np.genfromtxt(PATH + '/' + DIR + '/' + history, skip_header=5, names=True)
    axh.plot(h["center_h1"], h["mass_conv_core"], color = color, label = label, markeredgecolor = color, markerfacecolor = 'none', markeredgewidth = 0.5)
    axh2.plot(h["center_h1"], h["surface_mg24"]/h["surface_mg24"][0], '-o', color = color, label = label, markeredgecolor = color, markerfacecolor = 'none', markeredgewidth = 0.5)
    axh3.plot(h["log_Teff"], h["log_L"], color = color, label = label)


### Set by TA. ====
PATH     = '<path_to_folder_with_models>' # Path to where you create the folders to store the students' files, no trailing slash
DIR_lab1 = '' # Folder in which you store the students' output for microlab1, no trailing slash
DIR_lab3 = '' # Folder in which you store the students' output for microlab3, no trailing slash
microlab = '1' # '1' (Microlab 1) or '3' (Microlab 3)

#### ==============

### Microlab 1: Plot Brunt-Vaisala frequency squared, convective core mass, HR track, and mass fraction of Mg24.

if microlab == '1':

    ### Effect of time_delta_coeff

    figp, axp = plt.subplots()
    plt.subplots_adjust(left = 0.17, bottom = 0.18, top = 0.96, right = 0.94)
    figh, axh = plt.subplots()
    plt.subplots_adjust(left = 0.15, bottom = 0.18, top = 0.96, right = 0.94)
    figh2, axh2 = plt.subplots()
    plt.subplots_adjust(left = 0.18, bottom = 0.18, top = 0.96, right = 0.94)
    figh3, axh3 = plt.subplots()
    plt.subplots_adjust(left = 0.18, bottom = 0.18, top = 0.96, right = 0.94)

    plot_model(DIR = DIR_lab1, profile = 'profile_mdcX_tdcY_nomaxdt_Xc010.data', history = 'history_mdcX_tdcY_nomaxdt.data', axp = axp, axh = axh, axh2 = axh2, axh3 = axh3, color = 'purple', label = 'time_delta_coeff = Y')
    plot_model(DIR = DIR_lab1, profile = 'profile_mdcX_tdcY_nomaxdt_Xc010.data', history = 'history_mdcX_tdcY_nomaxdt.data', axp = axp, axh = axh, axh2 = axh2, axh3 = axh3, color = 'k', label = 'time_delta_coeff = Y')
    plot_model(DIR = DIR_lab1, profile = 'profile_mdcX_tdcY_nomaxdt_Xc010.data', history = 'history_mdcX_tdcY_nomaxdt.data', axp = axp, axh = axh, axh2 = axh2, axh3 = axh3, color = 'b', label = 'time_delta_coeff = Y')
    plot_model(DIR = DIR_lab1, profile = 'profile_mdcX_tdcY_nomaxdt_Xc010.data', history = 'history_mdcX_tdcY_nomaxdt.data', axp = axp, axh = axh, axh2 = axh2, axh3 = axh3, color = 'cyan', label = 'time_delta_coeff = Y')

    axp.set_xlabel(r'$r/R_\star$')
    axp.set_ylabel(r'$N^2~[10^6\cdot{\rm Hz}^2]$')
    axp.set_xlim(0.110, 0.135)
    axp.set_ylim(-0.1, 2)
    axp.legend()
    axh.set_xlabel(r'H mass fraction core, $X_{\rm c}$')
    axh.set_ylabel(r'$m_{\rm c}~[M_\odot]$')
    axh.invert_xaxis()
    axh.legend()
    axh2.set_xlabel(r'H mass fraction core, $X_{\rm c}$')
    axh2.set_ylabel(r'fraction initial $^{24}$Mg surf')
    axh2.invert_xaxis()
    axh2.legend()
    axh3.invert_xaxis()
    axh3.legend()
    axh3.set_xlabel(r'$\log(T_{\rm eff}/{\rm K})$')
    axh3.set_ylabel(r'$\log(L_{\star}/{\rm L}_\odot)$')

    figp.savefig('Effect_tdc_N2.png')
    figh.savefig('Effect_tdc_core-mass.png')
    figh2.savefig('Effect_tdc_abun.png')
    figh3.savefig('Effect_tdc_HRD.png')


### Microlab 3: Plot the HR tracks.
if microlab == '3':

    def plot_HR_track(PATH, dir, history, ax, label, color, linestyle):

        matrix = np.genfromtxt(PATH + '/' + dir + '/' + history, skip_header=5,names=True)

        # Load the columns of interest for an HR diagram
        log_L   = matrix["log_L"]
        log_Teff = matrix["log_Teff"]
        ax.plot(10**log_Teff, log_L, color = color, label = label, linestyle = linestyle)


    fig, ax = plt.subplots()
    plt.subplots_adjust(left = 0.18, bottom = 0.18, top = 0.98, right = 0.98)
    plot_HR_track(PATH = PATH, dir = DIR_lab3, history = 'history_<mixture>.data', ax = ax, color = 'r', label = r'<mixture>', linestyle = 'solid')
    plot_HR_track(PATH = PATH, dir = DIR_lab3, history = 'history_<mixture>.data', ax = ax, color = 'b', label = r'<mixture>', linestyle = 'solid')
    plot_HR_track(PATH = PATH, dir = DIR_lab3, history = 'history_<mixture>.data', ax = ax, color = 'k', label = r'<mixture>', linestyle = 'solid')
    plot_HR_track(PATH = PATH, dir = DIR_lab3, history = 'history_<mixture>.data', ax = ax, color = 'g', label = r'<mixture>', linestyle = 'solid')
    ax.text(5772, 0, r'$\odot$', color = 'k', horizontalalignment='center', verticalalignment='center') # The Sun
    ax.invert_xaxis()
    ax.legend()
    ax.set_xlabel(r'$T_{\rm eff}/{\rm K}$')
    ax.set_ylabel(r'$\log(L_{\star}/{\rm L}_\odot)$')
    fig.savefig('Effect_opacity_HRD.png')


plt.show(block = False)
