import React from 'react'

import './AboutTab.css';

export default function AboutTab({ channel }) {
    return (
        <div id='about-tab' className='row-top'>
            {channel.about && (
                <div id='about-tab-left' className='col-left'>
                    <h4>Description</h4>
                    <p style={{ fontSize: '14px' }}>{channel.about}</p>
                </div>

            )}
            <div id='about-tab-right' className='col-left'>
                <span style={{ paddingTop: '0' }}>Stats</span>
                <span>Joined {channel.createdAt}</span>
                {/* <span>[view count]</span> */}
            </div>
        </div>
    )
}
