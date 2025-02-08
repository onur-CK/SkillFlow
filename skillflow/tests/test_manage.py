"""
Tests for manage.py command-line handling
"""
from django.test import TestCase
from django.core.management import execute_from_command_line
from unittest.mock import patch
import os
import sys

class ManageCommandTests(TestCase):
    @patch('django.core.management.execute_from_command_line')
    def test_manage_execute_from_command_line(self, mock_execute):
        """Test that manage.py properly calls execute_from_command_line"""
        # Store original sys.argv
        orig_argv = sys.argv
        
        try:
            # Set up test arguments
            test_args = ['manage.py', 'help']
            sys.argv = test_args
            
            # Import and run manage.py
            with patch.dict(os.environ, {'DJANGO_SETTINGS_MODULE': 'skillflow.settings'}):
                import manage
                
            # Verify execute_from_command_line was called with correct args
            mock_execute.assert_called_once_with(test_args)
            
        finally:
            # Restore original sys.argv
            sys.argv = orig_argv

    @patch('django.core.management.execute_from_command_line')
    def test_manage_different_commands(self, mock_execute):
        """Test manage.py with different Django commands"""
        orig_argv = sys.argv
        
        test_cases = [
            ['manage.py', 'runserver'],
            ['manage.py', 'migrate'],
            ['manage.py', 'makemigrations'],
            ['manage.py', 'shell'],
            ['manage.py', 'collectstatic', '--noinput']
        ]
        
        try:
            for test_args in test_cases:
                sys.argv = test_args
                
                with patch.dict(os.environ, {'DJANGO_SETTINGS_MODULE': 'skillflow.settings'}):
                    import manage
                
                mock_execute.assert_called_with(test_args)
                mock_execute.reset_mock()
                
        finally:
            sys.argv = orig_argv

    @patch('django.core.management.execute_from_command_line')
    def test_manage_with_settings(self, mock_execute):
        """Test manage.py with different settings modules"""
        orig_argv = sys.argv
        settings_modules = [
            'skillflow.settings',
            'skillflow.settings.local',
            'skillflow.settings.production'
        ]
        
        try:
            for settings_module in settings_modules:
                test_args = ['manage.py', 'help']
                sys.argv = test_args
                
                with patch.dict(os.environ, {'DJANGO_SETTINGS_MODULE': settings_module}):
                    import manage
                
                mock_execute.assert_called_with(test_args)
                mock_execute.reset_mock()
                
        finally:
            sys.argv = orig_argv

    @patch('django.core.management.execute_from_command_line')
    def test_manage_error_handling(self, mock_execute):
        """Test manage.py error handling"""
        orig_argv = sys.argv
        
        try:
            # Test with invalid command
            test_args = ['manage.py', 'invalid_command']
            sys.argv = test_args
            
            with patch.dict(os.environ, {'DJANGO_SETTINGS_MODULE': 'skillflow.settings'}):
                import manage
            
            mock_execute.assert_called_with(test_args)
            
            # Test with missing settings
            with patch.dict(os.environ):
                if 'DJANGO_SETTINGS_MODULE' in os.environ:
                    del os.environ['DJANGO_SETTINGS_MODULE']
                
                with self.assertRaises(ImportError):
                    import manage
                    
        finally:
            sys.argv = orig_argv

    @patch('django.core.management.execute_from_command_line')
    def test_manage_with_options(self, mock_execute):
        """Test manage.py with various command options"""
        orig_argv = sys.argv
        
        test_cases = [
            ['manage.py', 'runserver', '8001'],
            ['manage.py', 'migrate', '--fake'],
            ['manage.py', 'collectstatic', '--noinput', '--clear'],
            ['manage.py', 'createsuperuser', '--username=admin'],
            ['manage.py', 'test', '--verbosity=2']
        ]
        
        try:
            for test_args in test_cases:
                sys.argv = test_args
                
                with patch.dict(os.environ, {'DJANGO_SETTINGS_MODULE': 'skillflow.settings'}):
                    import manage
                
                mock_execute.assert_called_with(test_args)
                mock_execute.reset_mock()
                
        finally:
            sys.argv = orig_argv