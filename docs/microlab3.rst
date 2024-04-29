Microlab 3: Opacities and initial mixture
===================================

Copy the test suite ``$MESA_DIR/star/test_suite/1M_pre_ms_to_wd`` somewhere outside ``$MESA_DIR``.

In ``&kap`` of ``inlist_start``, ``inlist_to_end_core_h_burn`` and ``inlist_to_start_he_flash`` change

.. code-block:: console

    kap_file_premix = ‘’ 
    ! Either gn93, gs98, a09, OP_gs98, or OP_a09_nans_removed_by_hand
    kap_lowT_prefix = ‘’ 
    ! Either lowT_fa05_gn93, lowT_fa05_gs98, or lowT_fa05_a09p


to a specific mixture. 

In ``&star_job`` of ``inlist_start`` add 

.. code-block:: console

    initial_zfracs = … ! 2 = GN93, 3 = GS98, 6 = A09 

.. tip::

    Full article references can be found in ``$MESA_DIR/chem/public/chem_def.f90``.

In ``&controls`` add

.. code-block:: console

    log_directory = ‘<your_mixture>’

In ``&controls`` of ``inlist_to_start_he_flash change`` change 

.. code-block:: console

    max_model_number = 500 

Run a model, plot ``log_Teff`` vs. ``log_L``, and compare the result with your table.  What is the impact of the opacity on the evolution track?
