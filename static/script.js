
    // Add some interactive effects
    document.addEventListener('DOMContentLoaded', function() {
      // Focus on amount field when page loads
      const amountField = document.getElementById('amount');
      if (amountField) amountField.focus();
      
      // Add animation to expense items
      const expenseItems = document.querySelectorAll('.expense-item');
      expenseItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.05}s`;
        item.style.animation = 'fadeIn 0.5s';
      });
      
      // Add confirmation for delete actions
      const deleteForms = document.querySelectorAll('form[action*="delete"]');
      deleteForms.forEach(form => {
        form.addEventListener('submit', function(e) {
          if (!confirm('Are you sure you want to delete this expense?')) {
            e.preventDefault();
          }
        });
      });
      
      // Highlight the active field
      const inputs = document.querySelectorAll('input');
      inputs.forEach(input => {
        input.addEventListener('focus', function() {
          this.parentElement.style.transform = 'translateY(-2px)';
        });
        
        input.addEventListener('blur', function() {
          this.parentElement.style.transform = 'translateY(0)';
        });
      });
    });
