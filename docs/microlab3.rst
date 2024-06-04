Microlab 3: Opacities and initial mixture
===================================

Copy the test suite ``$MESA_DIR/star/test_suite/1M_pre_ms_to_wd`` somewhere outside ``$MESA_DIR``. Once you are in the newly copied work directory, copy the following files into it

.. code-block:: console

    cp $MESA_DIR/star/test_suite/20M_pre_ms_to_core_collapse/r*_nomodfiles .

This test suite runs multiple inlists consecutively and these files will allow us to restart from a photo instead of a ``.mod`` file when running the next inlist.
Create a new file ``nano run_all`` (or any other text editor) and copy into it the following

.. code-block:: console

    ./rn_nomodfiles inlist_start_header
    ./re_nomodfiles . inlist_to_end_core_h_burn_header
    ./re_nomodfiles . inlist_to_start_he_core_flash_header

Finally, make this file executable with 

.. code-block:: console

    chmod +x run_all

In the ``&kap`` section of ``inlist_start``, ``inlist_to_end_core_h_burn`` and ``inlist_to_start_he_core_flash`` change

.. code-block:: console

    kap_file_prefix = ''     ! Either gn93, gs98, a09, OP_gs98, or OP_a09_nans_removed_by_hand
    kap_lowT_prefix = ''     ! Either lowT_fa05_gn93, lowT_fa05_gs98, or lowT_fa05_a09p
    kap_CO_prefix   = ''     ! Either gn93_co, gs98_co, or a09_co


to a specific mixture (i.e. the relative abundances of metals). Distribute the different options amongst your table, but use the same mixture for all three controls.

In the ``&star_job`` section of ``inlist_start`` add 

.. code-block:: console

    initial_zfracs = … ! 2 = GN93, 3 = GS98, 6 = A09 

using the corresponding mixture.

.. tip::

    Full article references can be found in ``$MESA_DIR/chem/public/chem_def.f90``.


In the ``&controls`` section of ``inlist_to_start_he_core_flash`` change 

.. code-block:: console

    max_model_number = 400 

Compile and run a model by ``./run_all``, plot ``log_Teff`` vs. ``log_L`` with `MESA Explorer <https://billwolf.space/mesa-explorer/>`__, and compare the result with your table. The history file will be in ``LOGS``. Give the history file a more appropriate name.

.. code-block:: console

    mv history.data history_<your_mixture>.data


Compare for example the highest effective temperature reached. What is the impact of the opacity on the evolution track?
