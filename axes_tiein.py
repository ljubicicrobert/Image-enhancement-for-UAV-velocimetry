# Used for all single-channel image plots
# Check out and try different colormaps at:
# https://matplotlib.org/3.5.1/tutorials/colors/colormaps.html
cmap = 'viridis'


# Callback function to simultaneously zoom all active axes
def on_lims_change(event_ax):
    cid_list = list(event_ax.callbacks.callbacks['ylim_changed'].keys())
    for cid in cid_list:
        event_ax.callbacks.disconnect(cid)

    fig = event_ax.get_figure()
    list_ca = fig.axes

    xlim = [int(x) for x in event_ax.get_xlim()]
    ylim = [int(y) for y in event_ax.get_ylim()]

    for a in list_ca:
        if a != event_ax:
            try:
                # Test to see if ax.imshow() was used
                a.get_images()[0]._A
                
                # If ax.imshow() then set lims
                a.set_xlim(xlim)
                a.set_ylim(ylim)
            except:
                # Otherwise do nothing
                continue

    event_ax.callbacks.connect('ylim_changed', on_lims_change)
