"""
Basic I/O Function: Sleep Endpoint
===================================
Simple endpoint that sleeps for a specified number of seconds.
"""

import json
import time


def handler(context, basicio):
    """
    Sleep endpoint that pauses for the specified duration.

    Parameters:
      - seconds: Number of seconds to sleep (0-30)
      - milliseconds: Number of milliseconds to sleep (0-30000)
      Provide one or the other, not both.

    Usage:
      ?seconds=5
      ?milliseconds=500
    """

    try:
        context.log('Sleep endpoint called')

        # Get parameters
        seconds_str = basicio.get_argument('seconds')
        milliseconds_str = basicio.get_argument('milliseconds')

        context.log(f'Parameters: seconds={seconds_str}, milliseconds={milliseconds_str}')

        # Validate exactly one parameter is provided
        if seconds_str and milliseconds_str:
            error = json.dumps({
                'error': 'Provide either seconds or milliseconds, not both',
                'usage': '?seconds=NUMBER or ?milliseconds=NUMBER'
            })
            basicio.write(error)
            context.close()
            return

        if not seconds_str and not milliseconds_str:
            error = json.dumps({
                'error': 'seconds or milliseconds parameter is required',
                'usage': '?seconds=NUMBER or ?milliseconds=NUMBER',
                'parameters': {
                    'seconds': 'Number of seconds to sleep (0-30)',
                    'milliseconds': 'Number of milliseconds to sleep (0-30000)'
                }
            })
            basicio.write(error)
            context.close()
            return

        # Parse the provided parameter
        if milliseconds_str:
            try:
                milliseconds = float(milliseconds_str)
            except ValueError:
                error = json.dumps({
                    'error': 'Invalid milliseconds parameter. Must be a number.',
                    'provided': milliseconds_str
                })
                basicio.write(error)
                context.close()
                return
            seconds = milliseconds / 1000.0
            unit = 'milliseconds'
            original_value = milliseconds
        else:
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
            unit = 'seconds'
            original_value = seconds
        
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
            'message': f'Slept for {original_value} {unit}',
            'slept_for': original_value,
            'unit': unit
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