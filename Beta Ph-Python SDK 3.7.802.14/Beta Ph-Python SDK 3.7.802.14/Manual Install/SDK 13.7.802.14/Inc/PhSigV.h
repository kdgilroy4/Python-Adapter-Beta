/*****************************************************************************/
//                                                                   
//  Copyright (C) 1992-2018 Vision Research Inc. All Rights Reserved.
//                                                                   
//  The licensed information contained herein is the property of     
//  Vision Research Inc., Wayne, NJ, USA  and is subject to change   
//  without notice.                                                  
//                                                                   
//  No part of this information may be reproduced, modified or       
//  transmitted in any form or by any means, electronic or           
//  mechanical, for any purpose, without the express written         
//  permission of Vision Research Inc.                               
//                                                                   
/*****************************************************************************/

#ifndef __PHSIGVINCLUDED__
#define __PHSIGVINCLUDED__

#ifdef __cplusplus
extern "C"
{
#endif

//Do not define neither _PHSIGV_ nor _NOPHSIGV_ in your program to allow
//compiler optimization
#if defined(_PHSIGV_)
#define EXIMPROC __declspec(dllexport)
#else
#define EXIMPROC __declspec(dllimport)
#endif


//for range.c
typedef enum
{
	RangeDataUnitsDegMinSec = 0,
	RangeDataUnitsDegrees = 1
}RANGE_DATA_UNITS;



// Function prototypes
EXIMPROC HRESULT PhSigSetup(UINT CN);

#ifdef __cplusplus
}
#endif

#undef EXIMPROC     //avoid conflicts with other similar headers
#endif