Microlab 2: Verifying hydrostatic equilibrium
===================================

We continue in the same work directory as Microlab 1. Copy the contents of ``star/job/standard_run_star_extras.inc`` into ``src/run_star_extras.f90`` in your work directory.

.. tip::

    You can use ``shmesa extras`` to fill in the ``run_star_extras.f90`` template.

In the subroutine ``data_for_extra_history_columns``, compute the following maximum residuals

.. math::

  \max \left( \frac{\left| \frac{\partial P} {\partial m} \right| - \left| \frac{Gm} {4 \pi r^4} \right| }{\left|  \frac{\partial P} {\partial m}  \right|} \right) 

Save these into a new history column named ``max_residuals``. (Do not forget to update ``how_many_extra_history_columns``.) Think about which quantities are defined on cells and which on faces.

.. tip::

    Some useful functions are ``ABS(array)``, ``MAXVAL(array)`` and ``pow4(x)``.

In the ``&controls`` section of ``inlist_1.5M_with_diffusion`` change 

.. code-block:: console

    num_trace_history_values = 3

and add

.. code-block:: console

    trace_history_value_name(3) = 'max_residuals'

Run the model. To what precision is hydrostatic equilibrium satisfied?



