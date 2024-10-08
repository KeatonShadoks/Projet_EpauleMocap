/*********************************************************************
 * \page   MarkerPositionCollection.cpp
 * \file   MarkerPositionCollection.cpp
 * \brief  
 *********************************************************************/
/* 
Copyright � 2014 NaturalPoint Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. */

#include "MarkerPositionCollection.h"

//////////////////////////////////////////////////////////////////////////
// MarkerPositionCollection implementation
//////////////////////////////////////////////////////////////////////////

MarkerPositionCollection::MarkerPositionCollection()
  :mMarkerPositionCount(0)
{
  ;
}

//////////////////////////////////////////////////////////////////////////
/// <summary>Appends the given marker positions to any existing marker positions
/// contained in self.
/// </summary>
/// <param name='markerData'>Array of marker x, y, z coordinates.<param>
/// <param name='numRigidBodies'>Number of markers.</param>
/// <remarks>The order of the marker positions is preserved.</remarks>
//////////////////////////////////////////////////////////////////////////
void MarkerPositionCollection::AppendMarkerPositions(float markerData[][3], size_t numMarkers)
{
  for (size_t i = 0; i < numMarkers; ++i)
  {
    mMarkerPositions[i + mMarkerPositionCount] = std::make_tuple(markerData[i][0], markerData[i][1], markerData[i][2]);
  }

  mMarkerPositionCount += numMarkers;
}

//////////////////////////////////////////////////////////////////////////
/// <summary>
/// Appends labeled marker data to any existing labeled marker data.
/// </summary>
/// <param name='markers'>Array of labeled marker data structures.</param>
/// <param name='numMarkers'>Number of labeled markers.</param>
//////////////////////////////////////////////////////////////////////////
void MarkerPositionCollection::AppendLabledMarkers(sMarker markers[], size_t numMarkers)
{
  for (size_t i = 0; i < numMarkers; ++i)
  {
    mLabledMarkers[i + mLabledMarkerCount].ID   = markers[i].ID;
    mLabledMarkers[i + mLabledMarkerCount].x    = markers[i].x;
    mLabledMarkers[i + mLabledMarkerCount].y    = markers[i].y;
    mLabledMarkers[i + mLabledMarkerCount].z    = markers[i].z;
    mLabledMarkers[i + mLabledMarkerCount].size = markers[i].size;
	mLabledMarkers[i + mLabledMarkerCount].params = markers[i].params;
  }

  mLabledMarkerCount += numMarkers;
}