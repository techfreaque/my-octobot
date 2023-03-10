# cython: language_level=3
#  Drakkar-Software OctoBot-Backtesting
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.

cdef class TimeManager:
    cdef object logger

    cdef dict config
    
    cdef public double starting_timestamp
    cdef public double finishing_timestamp
    cdef public double current_timestamp
    cdef public double time_interval

    cdef public bint time_initialized

    cdef public object timestamp_accept_check_callback
    cdef readonly list timestamps_whitelist
    cdef object _timestamps_whitelist_queue

    cpdef void initialize(self)
    cpdef void start(self)
    cpdef bint has_finished(self)
    cpdef object next_timestamp(self)    # object to allow exception raising
    cpdef void set_minimum_timestamp(self, double minimum_timestamp)
    cpdef void set_maximum_timestamp(self, double maximum_timestamp)
    cpdef void set_current_timestamp(self, double timestamp)
    cpdef double get_total_iteration(self)
    cpdef double get_remaining_iteration(self)
    cpdef void register_timestamp_whitelist(self, object timestamps, object check_callback, bint append_to_whitelist=*)

    cdef void _reset_time(self)
    cdef object _should_skip_current_timestamp(self)    # object to allow exception raising
    cdef bint _has_current_timestamp_in_whitelist(self)
