#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK14 warmup task 01 - using arbitrary arguments."""


import pet


class Dog(pet.Pet):
    """A dog class."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the Dog class.

        Args:
            has_shots(boolean): An optional boolean value.


        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
