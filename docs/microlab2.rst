Microlab 2: Verifying hydrostatic equilibrium
===================================

We continue in the same work directory as Microlab 1. You can decrease the resolution if the run time was long. Copy the contents of ``star/job/standard_run_star_extras.inc`` into ``src/run_star_extras.f90`` in your work directory.

.. tip::

    You can use ``shmesa extras`` to fill in the ``run_star_extras.f90`` template.

In the subroutine ``data_for_extra_history_columns``, compute the following maximum residuals

.. math::

  \max \left( \frac{\left| \frac{\partial P} {\partial m} \right| - \left| \frac{Gm} {4\,\pi\,r^4} \right| }{\left|  \frac{\partial P} {\partial m}  \right|} \right) 

You will have to do a loop over all nz-1 cells. Because we compute differences between two cells for the derivative of the pressure, we are left with one cell fewer, i.e. nz-1 cells.

.. tip::

    Some useful functions are ``ABS()``, ``MAXVAL()`` and ``pow4()``. Constants :math:`G` and :math:`\pi` are already defined as ``standard_cgrav`` and ``pi``, respectively. Furthermore, you will need ``s% dm``, ``s% m`` and ``s% r``. You can look up how to excess the total pressure through the ``star_info`` structure by searching in ``$MESA_DIR/star_data/public/star_data_step_work.inc``.

Start from the code snippet below and complete the missing parts. Save the max residuals into a new history column named ``max_residuals``. (Do not forget to update ``how_many_extra_history_columns``.) Think about which quantities are defined on cells and which on faces.   

.. code-block:: console

      subroutine data_for_extra_history_columns(id, n, names, vals, ierr)
         integer, intent(in) :: id, n
         character (len=maxlen_history_column_name) :: names(n)
         real(dp) :: vals(n), max_residuals
         integer, intent(out) :: ierr
         real(dp), allocatable :: residuals(:)
         integer :: k
         real(dp) :: lhs, rhs
         type (star_info), pointer :: s
         ierr = 0
         call star_ptr(id, s, ierr)
         if (ierr /= 0) return


         allocate(residuals(s% nz))
         do k = 2, s% nz
             ! (dP/dm)
             lhs = ...
             ! ((G m) / (4 Pi r^4))
             rhs = ... 
             residuals(k) =  ...
             
         end do

         max_residuals = ...
         ! Add code here to store max_residuals in a new history column. 


      end subroutine data_for_extra_history_columns

See the solutions tab, if you are really stuck.

In the ``&controls`` section of ``inlist_1.5M_with_diffusion`` change 

.. code-block:: console

    num_trace_history_values = 3

and add

.. code-block:: console

    trace_history_value_name(3) = 'max_residuals'

Recompile and run the model. To what precision is hydrostatic equilibrium satisfied? (The trace history files will appear after the ZAMS.)



