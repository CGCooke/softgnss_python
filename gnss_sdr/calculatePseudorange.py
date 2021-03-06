#!/usr/bin/python
#--------------------------------------------------------------------------
#                           SoftGNSS v3.0
# 
# Copyright (C) Darius Plausinaitis and Dennis M. Akos
# Written by Darius Plausinaitis and Dennis M. Akos
# Converted to Python by Colin Beighley
#--------------------------------------------------------------------------
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
#USA.
#--------------------------------------------------------------------------

import numpy as np
def calculatePseudorange(trackResults,msOfTheSignal,channelNumber,settings):
  travelTime = np.inf
  samplesPerCode = round(settings.samplingFreq \
                     / (settings.codeFreqBasis / settings.codeLength))
  travelTime = [trackResults[channelNumber].absoluteSample[msOfTheSignal[channelNumber]] \
                 / samplesPerCode]
  minimum = np.floor(min(travelTime))
  travelTime = travelTime - minimum + settings.startOffset
  pseudorange = tuple(travelTime*(settings.c/1000))
  return pseudorange
