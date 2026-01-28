"""
Basic I/O Function: Sleep Endpoint
===================================
Simple endpoint that sleeps for a specified number of seconds.
"""

import json
import time


def handler(context, basicio):
    """
    Sleep endpoint that pauses for the specified number of seconds.
    
    Parameters:
      - seconds: Number of seconds to sleep [required]
    
    Usage:
      ?seconds=5
    """
    
    try:
        context.log('Sleep endpoint called')
        
        # Get the 'seconds' parameter
        seconds_str = basicio.get_argument('seconds')
        
        context.log(f'Parameter: seconds={seconds_str}')
        
        # Validate required parameter
        if not seconds_str:
            error = json.dumps({
                'error': 'seconds parameter is required',
                'usage': '?seconds=NUMBER',
                'parameters': {
                    'seconds': 'Number of seconds to sleep (0-30)'
                }
            })
            basicio.write(error)
            context.close()
            return
        
        # Convert to float
        try:
            seconds = float(seconds_str)
        except ValueError:
            error = json.dumps({
                'error': 'Invalid seconds parameter. Must be a number.',
                'provided': seconds_str
            })
            basicio.write(error)
            context.close()
            return
        
        # Validate range
        if seconds < 0:
            error = json.dumps({
                'error': 'Seconds must be non-negative',
                'provided': seconds
            })
            basicio.write(error)
            context.close()
            return
        
        if seconds > 30:
            error = json.dumps({
                'error': 'Maximum sleep time is 30 seconds',
                'provided': seconds
            })
            basicio.write(error)
            context.close()
            return
        
        # Sleep for the specified duration
        context.log(f'Sleeping for {seconds} seconds')
        time.sleep(seconds)
        context.log(f'Sleep completed')
        
        # Build response
        response = json.dumps({
            'success': True,
            'message': f'Slept for {seconds} seconds',
            'slept_for': seconds
        }, indent=2)
        
        basicio.write(response)
        context.close()
        
    except Exception as e:
        context.log(f'Error: {e}')
        import traceback
        context.log(traceback.format_exc())
        
        error = json.dumps({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        })
        basicio.write(error)
        context.close()