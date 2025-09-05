import React, { useState, useEffect } from 'react';

const FlagComponent = () => {
  const [flag, setFlag] = useState('');
  const [displayedFlag, setDisplayedFlag] = useState('');
  const [loading, setLoading] = useState(true);
  const [animationComplete, setAnimationComplete] = useState(false);

  // Fetch the flag from the URL
  useEffect(() => {
    const fetchFlag = async () => {
      try {
        const response = await fetch('https://wgg522pwivhvi5gqsn675gth3q0otdja.lambda-url.us-east-1.on.aws/616363');
        const text = await response.text();
        setFlag(text.trim());
        setLoading(false);
      } catch (error) {
        console.error('Error fetching flag:', error);
        setLoading(false);
      }
    };

    fetchFlag();
  }, []);

  // Typewriter effect animation
  useEffect(() => {
    if (!loading && flag && !animationComplete) {
      let currentIndex = 0;
      
      const typewriterInterval = setInterval(() => {
        if (currentIndex < flag.length) {
          setDisplayedFlag(flag.substring(0, currentIndex + 1));
          currentIndex++;
        } else {
          clearInterval(typewriterInterval);
          setAnimationComplete(true);
        }
      }, 500); // Half second delay between characters

      return () => clearInterval(typewriterInterval);
    }
  }, [loading, flag, animationComplete]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <ul>
        {displayedFlag.split('').map((char, index) => (
          <li key={index}>{char}</li>
        ))}
      </ul>
    </div>
  );
};

export default FlagComponent;
