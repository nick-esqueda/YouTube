import React from 'react'
import loadingWheel from '../../static/icons/loading-wheel.gif';
import './LoadingWheel.css';

export default function LoadingWheel({ isCentered=true }) {
  return (
    <img 
      src={loadingWheel}
      alt='loading-wheel'
      className={'loading-wheel' + (isCentered ? ' absolute-center' : '')}
    />
  )
}
