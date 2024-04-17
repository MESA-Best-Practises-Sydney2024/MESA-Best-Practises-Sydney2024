Microlab 3: Opacities and initial mixture
===================================

Copy the test suite ``$MESA_DIR/star/test_suite/1M_pre_ms_to_wd`` somewhere outside ``$MESA_DIR``.

In ``&kap`` of ``inlist_start``, ``inlist_to_end_core_h_burn`` and ``inlist_to_start_he_flash change``

.. code-block:: console

    kap_file_premix = ‘’ 
    kap_lowT_prefix = ‘’

In ``&star_job`` of ``inlist_start`` add 

.. code-block:: console

    initial_z_fracs = … 

.. tip::

    Full article references can be found in ``$MESA_DIR/chem/public/chem_def.f90``.

In ``&controls`` add

.. code-block:: console

    log_directory = ‘<your_mixture>’

In ``&controls`` of ``inlist_to_start_he_flash change`` change 

.. code-block:: console

    max_model_number = 500 

Run a model and compare the result with your table. 
