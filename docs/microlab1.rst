Microlab 1: Convergence study
===================================

Copy the test suite ``$MESA_DIR/star/test_suite/1.5M_with_diffusion`` somewhere outside ``$MESA_DIR``.

In the ``&star_job`` section of ``inlist_1.5M_with_diffusion``, add

.. code-block:: console

    write_profile_when_terminate = .true. 
    filename_for_profile_when_terminate = 'LOGS/mdcX_tdcY_nomaxdt/profile_mdcX_tdcY_nomaxdt_Xc010.data'


In the ``&controls`` section of ``inlist_1.5M_with_diffusion``, add

.. code-block:: console

    star_history_name = 'history_mdcX_tdcY_nomaxdt.data'
    log_directory = 'LOGS/mdcX_tdcY_nomaxdt'
    time_delta_coeff = Y 
    xa_central_lower_limit_species(1) = 'h1' 
    xa_central_lower_limit(1) = 0.1 

If you study the effect of changing `time_delta_coeff`, then also add in the same ``&controls`` section
.. code-block:: console

    set_min_D_mix = .true.
    min_D_mix = 1d2 ! minimal chemical diffusion coefficient in cm^2/s

For both cases, change

.. code-block:: console

    D_mix_ignore_diffusion = 1d10 ! Don't do diffusion where Dmix > 10^10 cm^/s.
    mesh_delta_coeff = X
    max_years_for_timestep = 0    ! no maximum
    max_model_number = -1         ! no maximum


Each person at a table select a different value for ``mesh_delta_coeff`` between 0.2 and 2.0 (even table number), or a value for ``time_delta_coeff`` between 0.05 and 2.0 (odd table number). Set the other one equal to 0.5.

In the ``history_columns.list``, add

.. code-block:: console

    surface mg24

Compile and run the model. Afterwards, plot (with `MESA Explorer <https://billwolf.space/mesa-explorer/>`__) the following quantities. (The files are in the ``LOGS`` directory.)

For the effect of ``mesh_delta_coeff``:

1. ``radius`` vs. ``brunt_N2`` (profile) and 2. ``center_h1`` vs. ``mass_conv_core`` (history) 

For the effect of ``time_delta_coeff``:

1. ``log_Teff`` vs. ``log_L`` (history) and 2. ``center_h1`` vs. ``surface_mg24`` (history) 
 
Compare the results with those of the others at your table. How are these quantities affected? What resolution would be sufficient? 
