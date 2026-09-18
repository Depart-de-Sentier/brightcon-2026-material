import plotting_class as pc
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

demand_markers = ["s", "D"]

kwargs_for_demand_vector = {
    'hlines': [0],
    # 'legend_padding': 0.05,
    'keep_y': True,
    'sci_notation': True,
    'legend_ncol': 1,
    'turn_x_label': False,
    # 'x_label': 'year',
    'marker': demand_markers,
    'show_lines': False,
    'show_stem': True,
    'linewidth': 2,
    'markersize': 4,
    'title_loc': 'center',
    'skip_zeroes': True,
    # 'legend_position': 'below',
    'legend_position': 'upper center',
}

def color_func_shift_n(labels, shift=1):
     colors = sns.color_palette("colorblind", n_colors = shift + len(labels))
     colors = colors[shift:]
     return {label: color for label, color in zip(labels, colors)}

def get_proportionally_padded_range(df_sub, share_below=0.05, share_above=0.05, min_y=0):
    """Calculates padded (y_min, y_max) for a subset DataFrame."""
    if df_sub.empty:
        return None

    min_val = df_sub.min().min()
    max_val = df_sub.max().max()
    val_range = abs(max_val) + abs(min_val)

    denom = 1 - share_below - share_above
    y_min = min_val - val_range * share_below / denom if min_val < min_y else min_y
    y_max = max_val + val_range * share_above / denom

    return (y_min, y_max)

def construct_plot_config_for_dualaxis_subplot(df_dict, kwargs_dict, twin_cols=[], main_cols=[], share_y_range=False, share_x_range=False, annotations=None, main_kwargs={}, twin_kwargs={}):
    plot_configs = []

    padding_below_main = 0.05
    padding_above_main = 0.15
    padding_below_twin = 0.05
    padding_above_twin = 0.05
    padding_x_left = 2
    padding_x_right = 2

    # loop over DataFrames once to determine shared axis ranges
    shared_x_range = (1e12,-1e12)
    shared_main_y_range = (0,1e-12)
    shared_twin_y_range = (0,1e-12)
    for title, df in df_dict.items():
        if share_x_range:
            x_values = df.index.values
            left_x = min(min(x_values)-padding_x_left, shared_x_range[0])
            right_x = max(max(x_values)+padding_x_right, shared_x_range[1])
            shared_x_range = (left_x, right_x)

        if share_y_range:
            # separate main vs twin columns present in this DataFrame
            curr_twin_cols = [c for c in df.columns if c in twin_cols]
            if not main_cols: main_cols = [c for c in df.columns if c not in twin_cols]
    
            # calculate main y-axis range
            main_y_range = (
                get_proportionally_padded_range(df[main_cols], share_below=padding_below_main, share_above=padding_above_main)
                if main_cols
                else None
            )
            shared_main_y_range = (min([shared_main_y_range[0],main_y_range[0]]), max([shared_main_y_range[1],main_y_range[1]]))

            # calculate twin y-axis range
            twin_y_range = (
                get_proportionally_padded_range(df[curr_twin_cols], share_below=padding_below_twin, share_above=padding_above_twin)
                if curr_twin_cols
                else None
            )
            shared_twin_y_range = (min([shared_twin_y_range[0],twin_y_range[0]]), max([shared_twin_y_range[1],twin_y_range[1]]))

    for i, (title, df) in enumerate(df_dict.items()):
        # separate main vs twin columns present in this DataFrame
        curr_twin_cols = [c for c in df.columns if c in twin_cols]
        if not main_cols: main_cols = [c for c in df.columns if c not in twin_cols]

        if share_y_range:
            main_y_range = shared_main_y_range
            twin_y_range = shared_twin_y_range
        else:
            # calculate main y-axis range
            main_y_range = (
                get_proportionally_padded_range(df[main_cols], share_below=padding_below_main, share_above=padding_above_main)
                if main_cols
                else None
            )

            # calculate twin y-axis range
            twin_y_range = (
                get_proportionally_padded_range(df[curr_twin_cols], share_below=padding_below_twin, share_above=padding_above_twin)
                if curr_twin_cols
                else None
            )

        if share_x_range:
            x_axis_range = shared_x_range
        else:
            x_axis_range = (min(df.index.values)-padding_x_left, max(df.index.values)+padding_x_right)

        # create config dicts
        config_main = {
                'plotter': pc.ScatterPlotter(),
                'data': df[main_cols],
                'title': title,
                'y_axis_range': main_y_range,
                'x_axis_range': x_axis_range,
                }
        if annotations: config_main['annotations'] = annotations[i]
                
        config_main.update(kwargs_dict)
        if main_kwargs: config_main.update(main_kwargs)

        config_twin_unique = {
                'plotter': pc.ScatterPlotter(color_func=color_func_shift_n),
                'data': df[curr_twin_cols],
                'y_label': kwargs_dict["twin_y_label"],
                'title': '',
                'y_axis_range': twin_y_range,
                'x_axis_range': x_axis_range,
                }
                
        config_twin = {**kwargs_dict, **config_twin_unique, **twin_kwargs}

        # assign config dicts
        config_here = {
            "dual_axis": True,
            "config_1": config_main,
            "config_2": config_twin
        }
        
        plot_configs.append(config_here)
        
    return plot_configs

def construct_plot_config_for_vintage_subplot(df_dict, kwargs_dict, annotations=None, kwargs_extra={}):
    plot_configs = []

    for i, ((title, y_label), df) in enumerate(df_dict.items()):

        # create config dicts
        config_here = {
                'plotter': pc.ContributionPlotter(),
                'data': df,
                'title': title,
                'y_label': y_label,
                'hlines': [0],
                }
        if annotations: config_here['annotations'] = annotations[i]
                
        config_here.update(kwargs_dict)
        if kwargs_extra: config_here.update(kwargs_extra)

        plot_configs.append(config_here)
        
    return plot_configs

def plot_grid(plot_configs, ncols=2, nrows=None, figsize=None, sharex=False, sharey=False, gridspec_kw=None,
              suptitle=None, add_shared_legend=True, add_shared_colorbar=False, wspace=0.1,
              hspace=0.1, filepath=None, legend_ax='last', include_data=False):
    """
    Create a grid of subplots using BasePlotter subclasses, with one shared legend and/or colorbar.
    
    Each plot_config can have either:
    - Single plotter config (normal subplot)
    - Two plotter configs with "dual_axis": True (creates twinx axes)
    """
    nplots = len(plot_configs)
    if nrows is None:
        nrows = int(np.ceil(nplots / ncols))
    if figsize is None:
        figsize = (6 * ncols, 4 * nrows)

    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, sharex=sharex, sharey=sharey, gridspec_kw=gridspec_kw)
    axes = np.atleast_1d(axes).flatten()

    shared_legend_labels = {}
    colorbar_image = None  # Store the image mappable for shared colorbar

    for i, (ax, config) in enumerate(zip(axes, plot_configs)):
        # Check if this is a dual-axis configuration
        is_dual_axis = isinstance(config, dict) and config.get("dual_axis", False)
        
        if is_dual_axis:
            # Dual axis subplot
            config_1 = config["config_1"]
            config_2 = config["config_2"]
            
            ax2 = ax.twinx()
            
            for (axis, cfg) in [(ax, config_1), (ax2, config_2)]:
                plotter = cfg["plotter"]
                data = cfg["data"]
                kwargs = {k: v for k, v in cfg.items() if k not in ["plotter", "data"]}

                # Suppress individual colorbars if shared colorbar requested
                if add_shared_colorbar:
                    kwargs['colorbar'] = False

                # Add additional kwargs for keep_x, if not already provided
                if sharex is False and 'keep_x' not in kwargs:
                    kwargs['keep_x'] = False if i + 1 <= nplots - ncols else True
                
                # Plot on appropriate axis
                plotter.plot(data=data, ax=axis, add_legend=False, **kwargs)
                shared_legend_labels.update(plotter._legend_labels)
                
                # Store colorbar image if available
                if add_shared_colorbar and hasattr(plotter, '_im') and colorbar_image is None:
                    colorbar_image = plotter._im
        else:
            # Single axis subplot
            plotter = config["plotter"]
            data = config["data"]
            kwargs = {k: v for k, v in config.items() if k not in ["plotter", "data"]}

            # Suppress individual colorbars if shared colorbar requested
            if add_shared_colorbar:
                kwargs['colorbar'] = False

            # Add additional kwargs for keep_x and keep_y, if not already provided
            if sharex is False and 'keep_x' not in kwargs:
                kwargs['keep_x'] = False if i + 1 <= nplots - ncols else True
            if sharey is False and 'keep_y' not in kwargs:
                kwargs['keep_y'] = False if i%ncols > 0 else True

            # Plot subplot
            plotter.plot(data=data, ax=ax, add_legend=False, **kwargs)
            shared_legend_labels.update(plotter._legend_labels)
            
            # Store colorbar image if available
            if add_shared_colorbar and hasattr(plotter, '_im') and colorbar_image is None:
                colorbar_image = plotter._im

    # Remove unused axes if grid > plots
    for ax in axes[nplots:]:
        ax.remove()

    # Shared legend
    if add_shared_legend and shared_legend_labels:
        legend_axis = axes[nplots-1] if legend_ax == 'last' else axes[legend_ax]
        plotter._add_legend(ax=legend_axis, legend_labels=shared_legend_labels, **kwargs)

    # Shared colorbar
    if add_shared_colorbar and colorbar_image is not None:
        # Get colorbar label from last config if available
        colorbar_label = kwargs.get('colorbar_label', '')
        # Calculate width of colorbar based on figsize
        fig_width_inch = figsize[0]
        cbar_width_inch = 0.15
        cbar_width = cbar_width_inch / fig_width_inch
        # Set location of colorbar as [left, bottom, width, height]
        cax = fig.add_axes([0.92, 0.15, cbar_width, 0.7])
        cbar = fig.colorbar(colorbar_image, cax=cax)
        if colorbar_label:
            cbar.set_label(colorbar_label)

    # Adjust spacing
    fig.subplots_adjust(wspace=wspace, hspace=hspace)

    if suptitle:
        fig.suptitle(suptitle, fontweight="bold")

    # Export
    if filepath:
        if include_data:
            data_export = {}
            for config in plot_configs:
                if isinstance(config, dict) and config.get("dual_axis", False):
                    data_export[config["config_1"].get("title", "plot")] = config["config_1"]["data"]
                    data_export[config["config_2"].get("title", "plot")] = config["config_2"]["data"]
                else:
                    data_export[config.get("title", "plot")] = config["data"]
            _ = plotter.save(filepath, data=data_export, fig=fig)
        else: _ = plotter.save(filepath, fig=fig)

    plt.show()

    return

def plot_two_axes(config_1, config_2, figsize=None, suptitle=None, add_shared_legend=True, filepath=None):
    """
    Draw one plot (of given class) using the left y-axis and draws a second plot (of given class) using the right y-axis.
    """
    if figsize is None:
        figsize = (6, 4)

    # Create figure and axes
    fig, ax1 = plt.subplots(figsize=figsize)
    ax2 = ax1.twinx()

    shared_legend_labels = {}

    for (ax, config) in [(ax1, config_1), (ax2, config_2)]:
        plotter = config["plotter"]
        data = config["data"]
        kwargs = {k: v for k, v in config.items() if k not in ["plotter", "data"]}

        # Plot subplot, but suppress individual legends
        plotter.plot(data=data, ax=ax, add_legend=False, **kwargs)

        # Collect legend entries from each plotter
        shared_legend_labels.update(plotter._legend_labels)

    # Shared legend
    if add_shared_legend and shared_legend_labels:
        # Use function of BasePlotter to create legend
        plotter._add_legend(ax=ax1, legend_labels=shared_legend_labels, **kwargs)

    if suptitle:
        fig.suptitle(suptitle, fontweight="bold")

    # Export
    data_export = {config["title"] : config["data"] for config in [config_1, config_2]}
    if filepath: plotter.save(filepath, data=data_export)

    return fig, [ax1, ax2]