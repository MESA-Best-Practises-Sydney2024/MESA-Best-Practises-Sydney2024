Solution Microlab 2
===================================

.. code-block:: console

      integer function how_many_extra_history_columns(id)
         integer, intent(in) :: id
         integer :: ierr
         type (star_info), pointer :: s
         ierr = 0
         call star_ptr(id, s, ierr)
         if (ierr /= 0) return
         how_many_extra_history_columns = 1
      end function how_many_extra_history_columns

      subroutine data_for_extra_history_columns(id, n, names, vals, ierr)
         integer, intent(in) :: id, n
         character (len=maxlen_history_column_name) :: names(n)
         real(dp) :: vals(n), max_residuals
         integer, intent(out) :: ierr
         real(dp), allocatable :: residuals(:)
         integer :: k
         type (star_info), pointer :: s
         ierr = 0
         call star_ptr(id, s, ierr)
         if (ierr /= 0) return


         allocate(residuals(s% nz))
         do k = 2, s% nz
             ! |(dP/dm) / ((G m) / (4 Pi r^4))|
             residuals(k) = abs(((s% Peos(k-1) - s% Peos(k)) / ((s% dm(k-1) + s% dm(k)) / 2.0_dp)) / (standard_cgrav * s% m(k) / (4.0_dp * pi* pow4(s% r(k)))))
         end do
         max_residuals = 1._dp - MAXVAL(residuals)
         names(1) = 'max_residuals'
         vals(1)  = max_residuals


      end subroutine data_for_extra_history_columns
