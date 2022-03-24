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

#ifndef __PHSIGINCLUDED__
#define __PHSIGINCLUDED__

#ifdef __cplusplus
extern "C"
{
#endif

// Do not define neither _PHVIEW_ nor _NOPHVIEW_ in your program to allow
// compiler optimization

#if defined(_PHSIG_)
#define EXIMPROC __declspec(dllexport)
#elif !defined(_NOPHSIG_)
#define EXIMPROC __declspec(dllimport)
#else
#define EXIMPROC
#endif

#define GCI_SAMPLESPERIMAGE			2000	//Samples per image
#define GCI_BINCNT					2001	//Binary channels count
#define GCI_ANACNT					2002	//Analog channels count
#define GCI_SIGNAMECNT				2003	//Names and other properties available only for the first n signals (n=8)

#define GCI_ANABIPOLAR				2009	//global setting for analog (value signed or not)
#define GCI_ANADIFFERENTIAL			2010	//global setting for analog (differential inputs)
#define GCI_ANAENCODING				2011	//global setting for analog (encoding) 
											//(encoding: 0: 12 bit int, 1: 16 bit int, 2: 64 bit double)

#define GCI_SIGMODULENAME			2012	//Signal module name, global setting, read only
#define GCI_MAXBINCNT				2013	//Maximum binary channels count, read only
#define GCI_MAXANACNTSE				2014	//Maximum analog channels count, single ended mode, read only

#define GCI_UNIPOLARRANGES			2015	//count of analog gains in unipolar mode
#define GCI_BIPOLARRANGES			2016	//count of analog gains in bipolar mode
#define GCI_SUPPORTSSINGLEENDED		2017	//analog inputs supports single ended mode
#define GCI_SUPPORTSDIFFERENTIAL	2018	//analog inputs supports differential mode


#define GCI_SUPPORTEDGAINSU			2019	//obtain an array of supported analog gains in unipolar mode
#define GCI_SUPPORTEDGAINSB			2020	//obtain an array of supported analog gains in bipolar mode



//For PhGetCineInfo1()  PhSetCineInfo1()
#define GCI_BINNAME					2004	//Names for the specified binary channel
#define GCI_ANANAME					2005	//Names for the specified analog channel
#define GCI_ANAUNIT					2006	//Measurement units string for the specified analog channel
#define GCI_ANAGAIN					2007	//Analog gain for the specified analog channel, (int: 1, 2, 4, 8 ... 1000)
#define GCI_ANAUSERGAIN				2008	//User gain to convert the voltage value to measuring unit (double)



/*****************************************************************************/
// Error codes
#define ERR_BoardOverloaded				(-9801)
#define ERR_NoAnalogChannel             (-9803)
#define ERR_NoDigitalChannel			(-9804)
#define ERR_EmptyFIFOFailed				(-9805)
#define ERR_NoBoard						(-9806)
#define ERR_NoSigFile					(-9807)
#define ERR_EmptyBuffer					(-9808)
#define ERR_BadSigFile					(-9809)
#define ERR_BoardInternalError			(-9810)
#define ERR_EmptyBufferExceeded			(-9811)

#define ERR_BadChannelNumber			(-9820)

/*****************************************************************************/


#undef EXIMPROC     //avoid conflicts with other similar headers

#ifdef __cplusplus
}
#endif
#endif